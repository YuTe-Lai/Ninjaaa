MergeSort:
  把問題先拆解成子問題，並在逐一處理子問題後，將子問題的結果合併，如此便解決了原先的問題。 Merge Sort大概的步驟如下:
    1. 將數列分成兩個子數列。
    2. merge每一個子數列使之成為單一數列。




HeapSort:
將數列轉換成Max Heap，排序。將樹根(最大值)取出，並加入已排序數列。再重新做一次。





速度比較：
                	Merge Sort     	Heap Sort  	  
best case	      	  NlogN   	      NlogN   	      
average case        NlogN	          NlogN 	      
worst case	        NlogN  	        NlogN  	        





理論上heap sort 是in-place sorting , 也就是說它不像merge sort 每次method call 都需要去跟記憶體要一塊位置 , 
所以在處理上Heap sort 應該會比merge sort還要快速 。
