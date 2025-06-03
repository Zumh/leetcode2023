pub struct Solution; 
impl Solution {
    pub fn is_palindrome(x: i32) -> bool {

        if x < 0 {
            return false;
        }
       let mut reverse: i32 = 0;
       let mut original: i32 = x;

       while original > 0{
       
           let digits = original % 10;
           
/*
 // check for potential integer overflow
           if reverse > i32::MAX / 10 || (reverse == i32::MAX / 10 && digits > 7){
                return false;
           }
*/
           reverse = reverse * 10 + digits;


        
           original/=10;
       }

       x == reverse 

    }
}

fn main()
{
    let status = Solution::is_palindrome(121);

    println!("Solution: {}", status);


}
