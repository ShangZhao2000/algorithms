def find_median(arr1, arr2):
    def median(lst):
        return lst[len(lst) // 2] if len(lst) % 2 == 1 else (lst[(len(lst) // 2) - 1] + lst[len(lst) // 2]) / 2
    if not arr1:
        return median(arr2)
    if not arr2:
        return median(arr1)
    smaller_arr, larger_arr = arr1, arr2
    if len(larger_arr) < len(smaller_arr):
        smaller_arr, larger_arr = larger_arr, smaller_arr
    start = -1
    end = len(smaller_arr)
    while end >= start:
        cut_idx_smaller = (start + end) // 2
        cut_idx_larger = ((len(arr1) + len(arr2) + 1) // 2) - (cut_idx_smaller + 1) - 1
        left_cut_val_smaller = smaller_arr[cut_idx_smaller] if cut_idx_smaller >= 0 else float("-inf")
        right_cut_val_smaller = smaller_arr[cut_idx_smaller + 1] if cut_idx_smaller < len(smaller_arr) - 1 else float("inf")
        left_cut_val_larger = larger_arr[cut_idx_larger] if cut_idx_larger >= 0 else float("-inf")
        right_cut_val_larger = larger_arr[cut_idx_larger + 1] if cut_idx_larger < len(larger_arr) - 1 else float("inf")
        if left_cut_val_smaller <= right_cut_val_larger and left_cut_val_larger <= right_cut_val_smaller:
            break
        elif left_cut_val_smaller > right_cut_val_larger:
            end = cut_idx_smaller - 1
        else:
            start = cut_idx_smaller + 1
    if (len(arr1) + len(arr2)) % 2 == 1:
        return max(left_cut_val_smaller, left_cut_val_larger)
    else:
        return (max(left_cut_val_smaller, left_cut_val_larger) + min(right_cut_val_smaller, right_cut_val_larger)) / 2

