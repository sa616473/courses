// Put your solution here

function divideArray(nums){

    var tempEven = [];
    var tempOdd = [];

    for (var i=0; i< nums.length; i++){
        // console.log(i)
        if (nums[i] % 2 == 0)
            tempEven.push(nums[i])
        else
            tempOdd.push(nums[i])

    }


    tempEven.sort(function(a, b){return a - b});
    tempOdd.sort(function(a, b){return a - b});
    console.log("Even numbers:")

    if (tempEven.length < 1){
        console.log("None")
    }

    else {
        for (var i = 0; i < tempEven.length; i++){

            console.log(tempEven[i]);
        }
    }

    console.log("Odd numbers:")

    if(tempOdd.length < 1){
        console.log("None")
    }

    else{
        for (var i = 0; i < tempOdd.length; i++){
            console.log(tempOdd[i]);
        } 
    }

}