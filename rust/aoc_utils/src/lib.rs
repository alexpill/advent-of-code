/// Gets the input filename based on the current source file.
///
/// This macro expands at the call site, so `file!()` will correctly
/// reference the calling file, not this library file.
///
/// # Arguments
/// * `small` - If true, returns the small input filename, otherwise returns the full input filename
///
/// # Example
/// ```
/// let filename = aoc_utils::get_input_filename!(true);
/// ```
#[macro_export]
macro_rules! get_input_filename {
    ($small:expr) => {{
        let current_dir = std::env::current_dir().unwrap();
        let current_file = file!().split("/").last().unwrap();
        let file = current_file.replace(
            ".rs",
            if $small {
                "_input_small.txt"
            } else {
                "_input.txt"
            },
        );
        format!("{}/{}", current_dir.display(), file)
    }};
}
