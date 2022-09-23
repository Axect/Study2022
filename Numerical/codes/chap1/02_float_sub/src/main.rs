use peroxide::fuga::*;

fn main() {
    let n_vec = (-20 .. -9).collect::<Vec<_>>();
    let results = n_vec.iter().map(|&n| gen_subs(n)).collect::<Vec<_>>();

    let mut fl_sub = vec![0f64; n_vec.len()];
    let mut true_sub = vec![0f64; n_vec.len()];

    for (i, res) in results.into_iter().enumerate() {
        let (fl, tr) = res;
        fl_sub[i] = fl;
        true_sub[i] = tr;
    }

    let mut df = DataFrame::new(vec![]);
    df.push("n", Series::new(n_vec));
    df.push("fl_sub", Series::new(fl_sub));
    df.push("true_sub", Series::new(true_sub));

    df.print();

    df.write_nc("data/02_float_sub.nc").expect("Write Error");
}

fn gen_subs(n: i32) -> (f64, f64) {
    let delta = 10f64.powi(n);
    let x = 1e+17 * (1f64 + delta);
    let y = 1e+17;

    (x - y, 10f64.powi(n + 17))
}
