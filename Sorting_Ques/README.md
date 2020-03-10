# Sorting 

Sorting refers to arranging data in a particular format. Sorting algorithm specifies the way to arrange data in a particular order. Most common orders are in numerical or lexicographical order.

The importance of sorting lies in the fact that data searching can be optimized to a very high level, if data is stored in a sorted manner.

## In-place Sorting and Not-in-place Sorting
Sorting algorithms may require some extra space for comparison and temporary storage of few data elements. These algorithms do not require any extra space and sorting is said to happen in-place, or for example, within the array itself. This is called **in-place sorting**. Bubble sort is an example of in-place sorting.

However, in some sorting algorithms, the program requires space which is more than or equal to the elements being sorted. Sorting which uses equal or more space is called not-in-place sorting. Merge-sort is an example of **not-in-place sorting**.

## 1 Bubble Sort

Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

![ExaltedInconsequentialDwarfrabbit-size_restricted](https://user-images.githubusercontent.com/44902363/76322053-e15bcf00-6308-11ea-9959-8d2bc289c3e7.gif)

* **Worst complexity: n^2**
* **Average complexity: n^2**
* **Best complexity: n**
* **Space complexity: 1**
* **Method: Exchanging**
* **Stable: Yes**
* **Class: Comparison sort**

## 2 Selection Sort

Selection sort is a simple sorting algorithm. This sorting algorithm is an in-place comparison-based algorithm in which the list is divided into two parts, the sorted part at the left end and the unsorted part at the right end. Initially, the sorted part is empty and the unsorted part is the entire list.

The smallest element is selected from the unsorted array and swapped with the leftmost element, and that element becomes a part of the sorted array. This process continues moving unsorted array boundary by one element to the right.

This algorithm is not suitable for large data sets as its average and worst case complexities are of Ο(n2), where n is the number of items.

![selectionSort](https://user-images.githubusercontent.com/44902363/76322841-e1100380-6309-11ea-96c3-2562e1b95662.gif)

* **Worst complexity: n^2**
* **Average complexity: n^2**
* **Best complexity: n^2**
* **Space complexity: 1**
* **Method: Selection**
* **Stable: No**
* **Class: Comparison sort**

## 3 Insertion Sort

This is an in-place comparison-based sorting algorithm. Here, a sub-list is maintained which is always sorted. For example, the lower part of an array is maintained to be sorted. An element which is to be 'insert'ed in this sorted sub-list, has to find its appropriate place and then it has to be inserted there. Hence the name, insertion sort.

The array is searched sequentially and unsorted items are moved and inserted into the sorted sub-list (in the same array). This algorithm is not suitable for large data sets as its average and worst case complexity are of Ο(n2), where n is the number of items.

![Insertion-sort-example](https://user-images.githubusercontent.com/44902363/76323451-be321f00-630a-11ea-80dc-6bfd0acd655a.gif)

* **Worst complexity: n^2**
* **Average complexity: n^2**
* **Best complexity: n**
* **Space complexity: 1**
* **Method: Insertion**
* **Stable: Yes**
* **Class: Comparison sort**

## 4 Merge Sort

Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.

![Merge-sort-example-300px](https://user-images.githubusercontent.com/44902363/76325189-110cd600-630d-11ea-9b72-e60ad0d8d05e.gif)


* **Worst complexity: n*log(n)**
* **Average complexity: n*log(n)**
* **Best complexity: n*log(n)**
* **Space complexity: n**
* **Method: Merging**
* **Stable: Yes**

## 5 Quick Sort

Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.

* Always pick first element as pivot.
* Always pick last element as pivot (implemented below)
* Pick a random element as pivot.
* Pick median as pivot.
The key process in quickSort is partition(). Target of partitions is, given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time.


![PleasantCloseEyelashpitviper-size_restricted](https://user-images.githubusercontent.com/44902363/76326058-1880af00-630e-11ea-9b52-a9219584ef1e.gif)


* **Worst complexity: n^2**
* **Average complexity: n*log(n)**
* **Best complexity: n*log(n)**
* **Method: Partitioning**
* **Stable: No**
* **Class: Comparison sort**




