use std::io;
fn main() {
  println!("Enter nth fibonacci number: ");
  let mut nth = String::new();
  io::stdin()
    .read_line(&mut nth)
    .expect("failed to read");
  let nth: i32= nth.trim().parse().expect("cant convert");
  print_nth_fibonacci(nth);


}

fn print_nth_fibonacci(value:i32) {

let mut a = 0;
let mut b = 1;
let mut sum:i32=0;
for _i in 1..=value-2 {
    sum = a+b;
    a = b;
    b = sum;
}
println!("{}",sum);

    
}
