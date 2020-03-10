# Searching

Searching Algorithms are designed to check for an element or retrieve an element from any data structure where it is stored. Based on the type of search operation, these algorithms are generally classified into two categories:

* 1 **Sequential Search:** In this, the list or array is traversed sequentially and every element is checked. For example: **Linear Search.**

* 2 **Interval Search:** These algorithms are specifically designed for searching in sorted data-structures. These type of searching algorithms are much more efficient than Linear Search as they repeatedly target the center of the search structure and divide the search space in half. For Example: **Binary Search.**

## Linear Search:-

Linear search is a very simple search algorithm. In this type of search, a sequential search is made over all items one by one. Every item is checked and if a match is found then that particular item is returned, otherwise the search continues till the end of the data collection.

![VigorousSimpleArawana-size_restricted](https://user-images.githubusercontent.com/44902363/76320308-82955600-6306-11ea-98c8-357fd627c465.gif)


* **Worst complexity: O(n)**
* **Average complexity: O(n)**
* **Space complexity: O(1)**
* **Worst-case space complexity: O(1) iterative**

## Binary Search:-

Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

![bePceUMnSG-binary_search_gif](https://user-images.githubusercontent.com/44902363/76320758-1ff08a00-6307-11ea-8df8-ceded866158f.gif)

* **Worst complexity: O(log n)**
* **Average complexity: O(log n)**
* **Best complexity: O(1)**
* **Space complexity: O(1)**
* **Data structure: Array**
