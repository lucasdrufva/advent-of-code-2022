use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn calc_score(list: &Vec<u32>, height: u32) -> u32 {
    return match list.iter().position(|x| x >= &height) {
        Some(expr) => expr+1,
        None => list.len(),
    } as u32;

}

fn calc_visible(grid: &Vec<Vec<u32>>, x: usize, y: usize) -> (bool, u32) {
    let height = grid[x][y];

    let up = &grid[0..x].iter().rev().map(|l| l[y]).collect::<Vec<u32>>();
    let down = &grid[(x+1)..grid.len()].iter().map(|l| l[y]).collect::<Vec<u32>>();
    let right = &grid[x][(y+1)..grid[x].len()].to_vec();
    let left = &grid[x][0..y].to_vec().into_iter().rev().collect::<Vec<u32>>();

    let score = calc_score(up, height) * 
        calc_score(down, height) * 
        calc_score(left, height) * 
        calc_score(right, height);

    let visible = up.iter().all(|x| x < &height) || down.iter().all(|x| x < &height) || left.iter().all(|x| x < &height) || right.iter().all(|x| x < &height);

    return (visible, score);
}


fn main() {
    let mut grid: Vec<Vec<u32>> = Vec::new();

    if let Ok(lines) = read_lines("./input8.txt") {
        // Consumes the iterator, returns an (Optional) String
        for (i, line) in lines.enumerate() {
            grid.push(Vec::new());
            if let Ok(ip) = line {
                for c in ip.chars(){
                    grid[i].push(c.to_digit(10).unwrap());
                }
            }
        }
    }
    
    let mut visible_count:u32 = 0;
    let mut max_score: u32 = 0;

    for (i, _) in grid.iter().enumerate(){
        for (j,_) in grid[i].iter().enumerate(){
            let res = calc_visible(&grid, i, j);
            if res.0 {
                visible_count += 1;
            }
            if res.1 > max_score {
                max_score = res.1;
            }
        }
    }

    println!("Part 1: {}", visible_count);
    println!("Part 2: {}", max_score);
}

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
