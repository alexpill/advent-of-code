
fn get_input(small: bool) -> Vec<(u64, u64)> {
    let file = aoc_utils::get_input_filename!(small);
    std::fs::read_to_string(&file)
        .expect("Failed to read file")
        .replace("\n", "")
        .split(",")
        .map(|line| {
            let parts = line.split('-').collect::<Vec<&str>>();
            (
                parts[0].parse::<u64>().unwrap(),
                parts[1].parse::<u64>().unwrap(),
            )
        })
        .collect()
}

fn part1(input: &Vec<(u64, u64)>) -> u64 {
    let mut invalid_id_sum = 0;
    for (start, stop) in input {
        for id in *start..=*stop {
            let id_str = id.to_string();
            let id_len = id_str.len() / 2;
            if id_str[..id_len] == id_str[id_len..] {
                invalid_id_sum += id;
            }
        }
    }
    invalid_id_sum
}

fn part2(input: &Vec<(u64, u64)>) -> u64 {
    let mut invalid_id_sum = 0;
    for (start, stop) in input {
        for id in *start..=*stop {
            let id_str = id.to_string();
            let id_len = id_str.len();
            for pattern_len in 1..=id_len / 2 {
                if id_len % pattern_len == 0 {
                    let pattern = &id_str[..pattern_len];
                    let repeat_count = id_len / pattern_len;
                    if pattern.repeat(repeat_count) == id_str {
                        invalid_id_sum += id;
                        break;
                    }
                }
            }
        }
    }
    invalid_id_sum
}

fn main() {
    let input_small = get_input(true);
    println!("First part small: {}", part1(&input_small));
    println!("Second part small: {}", part2(&input_small));

    println!("--------------------------------");

    let input = get_input(false);
    println!("First part: {}", part1(&input));
    println!("Second part: {}", part2(&input));
}

// Results:
// First part: 18700015741
//Second part: 20077272987
