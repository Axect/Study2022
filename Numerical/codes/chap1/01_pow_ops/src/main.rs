use peroxide::fuga::*;

fn main() -> Result<(), Box<dyn Error>> {
    let x_vec = seq(0.99, 1.01, 0.0001);

    let p_vec = x_vec.fmap(p);
    let q_vec = x_vec.fmap(q);
    let r_vec = x_vec.fmap(r);

    let mut df = DataFrame::new(vec![]);
    df.push("x", Series::new(x_vec));
    df.push("p", Series::new(p_vec));
    df.push("q", Series::new(q_vec));
    df.push("r", Series::new(r_vec));

    df.print();

    df.write_nc("data/01_pow.nc")?;
    Ok(())
}

/// (1-x)^8 by pow operator
fn p(x: f64) -> f64 {
    (1f64 - x).powi(8)
}

/// expand (1-x)^8 without pow operator
fn q(x: f64) -> f64 {
    let mut s = 0f64;
    let mut x_term = x;
    for i in 0 .. 9 {
        s += C(8, i) as f64 * x_term;
        x_term *= -x;
    }
    s
}

/// expand (1-x)^8 with pow operator
fn r(x: f64) -> f64 {
    let mut s = 0f64;
    for i in 0 .. 9 {
        s += C(8, i) as f64 * (-x).powi(i as i32);
    }
    s
}
