"""

Defines two classes: Dictionary and Statistics.

Dictionary defines an implementation of a Python dictionary.

Statistics facilitates the statistical analysis of the performance of the dictionary with varying arguments.
"""

__author__ = "Shangbo Zhao"






from referential_array import ArrayR
from hash_table import LinearProbeHashTable
import timeit
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Dictionary:
    def __init__(self, hash_base: int, table_size: int) -> None:
        """ Initialises instance variables self.hash_table and self.load_time

            @Complexity: O(N) where N is table size
        """
        self.hash_table = LinearProbeHashTable(hash_base, table_size)
        self.load_time = 0

    def load_dictionary(self, filename: str, time_limit: int = None) -> int:
        """ Reads the words in the file given as input into a hash table, stopping when
        the time limit, if provided, is reached.

            @Complexity: O(N) where N is the number of lines in the file
            @Throws: TimeoutError if runtime exceeds time_limit
        """
        start_time = timeit.default_timer() #Starts timing
        words_added = 0
        f = open(filename, "r", encoding = "utf8")
        for line in f:
            self.hash_table.__setitem__(line.strip('\n'), 1)    #Adds each word in the file with the associated value 1
            words_added += 1    #Keeps record of how many words are added
            current_time = timeit.default_timer()   #Stops timing
            if time_limit != None and current_time - start_time > time_limit:
                raise TimeoutError  #Raises TimeoutError if recorded time exceeds time limit
        f.close()
        self.load_time = current_time - start_time  #Stores recorded time in self.load_time
        return words_added

    def add_word(self, word: str) -> None:
        """ Adds a word to the hash table with associated value of 1.

            @Complexity: Same as self.hash_table.__setitem__()
        """
        self.hash_table.__setitem__(word.lower(), 1)

    def find_word(self, word: str) -> bool:
        """ Returns boolean value indicating if the hash table contains the input word
        converted to lower case.

            @Complexity: Same as self.hash_table.__contains__()
        """
        return self.hash_table.__contains__(word.lower())

    def delete_word(self, word: str) -> None:
        """ Deletes input word converted to lower case from the hash table.

            @Complexity: Same as self.hash_table.__delitem__()
        """
        self.hash_table.__delitem__(word.lower())

    def menu(self) -> None:
        """ Prompts user with a menu allowing the selection of different dictionary functionalities.
        Carries out the selections and re-prompts the user until the user chooses to exit.

            @Complexity: O(1)
        """
        number = 0
        while number != 5:
            number = input("1. Read File\n2. Add Word\n3. Find Word\n4. Delete Word\n 5. Exit\nEnter option: ")
            if number == 1:
                file_name = input("Enter filename: ")
                self.load_dictionary(file_name)
                print("Successfully read file")
            elif number == 2:
                word = input("Enter word: ")
                self.add_word(word)
                print("[" + word + "]" + " Successfully added")
            elif number == 3:
                word = input("Enter word: ")
                try:
                    self.find_word(word)
                    print("[" + word + "]" + " Found in dictionary")
                except:
                    print("Invalid word")
            elif number == 4:
                word = input("Enter word: ")
                try:
                    self.delete_word(word)
                    print("[" + word + "]" + "Deleted from dictionary")
                except:
                    print("Invalid word")
            elif number == 5:
                print("Process finished with exit code 0")
            else:
                print("Invalid number, please try again.")

class Statistics:
    def load_statistics(self, hash_base: int, table_size: int, filename: str, max_time: int) -> tuple:
        """ Creates a dictionary instance and loads the input file while max_time is not exceeded by 
        runtime of the method. Returns a tuple containing various statistics regarding the performance
        of the dictionary.

            @Complexity: O(N) where N is the number of lines in the file read into the dictionary
            @Throws: TimeoutError if runtime exceeds max_time
        """
        dict_object = Dictionary(hash_base, table_size)
        try:
            words = dict_object.load_dictionary(filename, max_time)
            time = dict_object.load_time
        except TimeoutError:
            words = dict_object.hash_table.count
            time = max_time
        return (words, time) + dict_object.hash_table.statistics()
    def table_load_statistics(self, max_time: int) -> None:
        """ Loads different files into hash tables created with various combinations of different
        values of hash base and table size, generating summary statistics for each such combination
        and writing them to a csv file.

            @Complexity: O(N) where N is the combined number of lines in all of the text files
        """
        texts = ["english_small.txt", "english_large.txt", "french.txt"]
        b = [1, 27183, 250726]
        tablesize = [250727, 402221, 1000081]
        with open('output_task2.csv', mode='w') as f:
            file_writer = csv.writer(f, delimiter=',')
            file_writer.writerow(['filename', 'hash_base', 'table_size', 'words', 'time', 'collision_count', 'probe_total', 'probe_max', 'rehash_count'])
            for filename in texts:
                for hash_base in b:
                    for table_size in tablesize:
                        stats = self.load_statistics(hash_base, table_size, filename, max_time)
                        file_writer.writerow((filename, hash_base, table_size) + stats)

#s = Statistics()
#s.table_load_statistics(10)
df = pd.read_csv("output_task2.csv")

N = 9
english_small = list(df.loc[df['filename'] == 'english_small.txt']['time'])
english_large = list(df.loc[df['filename'] == 'english_large.txt']['time'])
french = list(df.loc[df['filename'] == 'french.txt']['time'])

ind = np.arange(N)
width = 0.2
x_ticks = []

hash_base_column = list(df['hash_base'])
table_size_column = list(df['table_size'])
for i in range(9):
    tick = 'B = ' + str(hash_base_column[i]) + ', TS = ' + str(table_size_column[i])
    x_ticks.append(tick)

plt.bar(ind, english_small, width, label = 'english_small.txt')
plt.bar(ind + width, english_large, width, label = 'english_large.txt')
plt.bar(ind + 2 * width, french, width, label = 'french.txt')

plt.xticks(ind + width, x_ticks, rotation = 20)
plt.title('Run Times')

plt.legend(loc = 'best')


plt.show()
#