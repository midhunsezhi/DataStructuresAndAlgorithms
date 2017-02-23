function solution(arr) {
	var currentIndex =1,
		start,
		stop,
		tempArr = [],
		declineStarted,
		gunthaCreated,
		sum = 0;


	while (currentIndex < arr.length -1) {
		start = currentIndex;
		declineStarted = false
		gunthaCreated = false;
		while (currentIndex < arr.length -1 && arr[currentIndex] <= arr[currentIndex -1]) {
			declineStarted = true;
			currentIndex++;
		}
		if (declineStarted) {
			while (currentIndex < arr.length - 1 && arr[currentIndex] >= arr[currentIndex - 1]) {
				gunthaCreated = true;
				currentIndex++;
			}
		}
		
		if(gunthaCreated) {
			stop = currentIndex - 1;
			minEdge = Math.min(arr[start], arr[stop])
			for (var j=start; j < stop; j++) {
				sum += Math.max(minEdge - arr[j], 0);
			}
		} else {
			currentIndex++;
		}
	}
	console.log(sum)
	return sum;
}

solution([0,1,0,2,1,0,1,3,2,1,2,1]);