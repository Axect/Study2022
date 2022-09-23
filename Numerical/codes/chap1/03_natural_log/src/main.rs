use peroxide::fuga::*;

fn main() {
    let x = seq(0, 1e-14, 1e-16);
    let y1 = x.fmap(|t| (1f64 + t).ln());
    let y2 = x.fmap(ln_fix);

    let mut df = DataFrame::new(vec![]);
    df.push("x", Series::new(x));
    df.push("y1", Series::new(y1));
    df.push("y2", Series::new(y2));

    df.print();

    df.write_nc("data/natural_log.nc").unwrap();
}

fn ln_fix(x: f64) -> f64 {
    if (1f64 + x) == 1f64 {
        x
    } else {
        (x * (1f64 + x).ln()) / (1f64 + x - 1f64)
    }
}
