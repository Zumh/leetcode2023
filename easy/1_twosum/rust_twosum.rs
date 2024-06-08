use std::collections::HashMap;

// Time complexity is O(n)
fn _two_sum_non_brute(nums: Vec<i32>, target: i32)-> Vec<i32>{
    let mut num_to_index = HashMap::new();

    for(index, &num) in nums.iter().enumerate(){
        
        let complement = target - num;

        if let Some(&complement_index) = num_to_index.get(&complement) {
            return vec![complement_index as i32, index as i32];
        }

        num_to_index.insert(num, index);
    }

    // If no solution is found (though the problem guarantees there is one)
    vec![]
}

fn two_sum_brute(nums: Vec<i32>, target: i32)-> Vec<i32>{
    for i in 0..nums.len(){
        for j in (i+1)..nums.len(){
            if nums[i] + nums[j] == target{
                return vec![i as i32, j as i32];
            }
        }
    }

    // If no solution is found (though the problem guarantees there is one)
    vec![]
}

fn main(){
    let nums = vec![2, 7, 11, 15];
    let target = 9;
    let result = two_sum_brute(nums, target);
    //let result = two_sum_non_brute(nums, target);
    println!("Indices: {:?}", result);
}