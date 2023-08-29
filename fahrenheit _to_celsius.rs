use std::io;
fn main() {
  println!("Enter Farenheight ");
  let mut farenheight = String::new();
  io::stdin()
    .read_line(&mut farenheight)
    .expect("failed to read");
  let farenheight: f32= farenheight.trim().parse().expect("cant convert");
  convert_celsius(farenheight);


}

fn convert_celsius(value:f32) {

let celsius = ((value-32.0)*5.0)/9.0;
println!("Celsius: {}",celsius);

    
}
