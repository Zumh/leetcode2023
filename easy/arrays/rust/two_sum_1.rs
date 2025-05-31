/*
 * find indexes of two number sum to the target 
 * a + b = target
 * [index1, index2]
 *
 * */
use std::collections::HashMap;

pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut result: Vec<i32> = vec![];
    let mut differences: HashMap<i32, i32> = HashMap::new();

    for (index, &current_number) in nums.iter().enumerate(){
        
        let current_difference = target - current_number;

        if let Some(&matching_index) = differences.get(&current_difference){
            // Found a pair that sums to target
            result.push(matching_index);
            // safe cast since array indices fit in 32
            result.push(index as i32); 
            return result;
        }
    
        // Insert current number and its index
        differences.insert(current_number, index as i32);
    } 
    result
}

fn main(){
    let nums: Vec<i32> = vec![2,7,11,15];
    let target: i32 = 9;

    println!("{:?}", two_sum(nums, target));
}
