#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <assert.h>

#define FILE_PATH "Day4Input.txt"
#define TEST_FILE_PATH "Day4TestInput.txt"

#define TARGET "XMAS"

#define ROW_END '\n'

int unixgetchar(FILE *file);                                                      // Returns only '\n' compared to '\r\n' for NT platforms, otherwise functionally the same as `fgetc(file)`.
char *str_reverse(char word[], size_t str_len);                                   // Reverses the given string (char array) in-place, keeping the last char (presumably, '\0') unchanged. Returns pointer to first item of array `row`.
int row_filler(char *row[], FILE *file, size_t *row_len);                         // Fills a `row` with chars from `file`, and updates the value of `row_len` if need be.
void row_printer(char row[], size_t row_len);                                     // Prints out the `row`, character-by-character.
int word_checker(char **rows, size_t word_len, size_t row_len, size_t row_count); // Find the frequency of the TARGET in the grid (`rows`) passed in.

/* ******** TARGET WORD FINDING HELPER FUNCTIONS ******** */

int word_validator(char word[], size_t word_len);                                                                 // Checks whether the passed in `word` matches `TARGET` (forwards AND backwards, with the `backwards` reversing the string in-place). Does NOT reverse the string back.
int horizontal_word_checker(char word[], char row[], int offset, size_t word_len);                                // Checks if the `word` matches `TARGET` horizontally to the right.
int vertical_word_checker(char word[], char *rows[], int current_row, int current_column, size_t word_len);       // Checks if the `word` matches the `TARGET` straight down.
int diagonal_left_word_checker(char word[], char *rows[], int current_row, int current_column, size_t word_len);  // Checks if the `word` matches the `TARGET` from the current spot to the diagonal bottom left.
int diagonal_right_word_checker(char word[], char *rows[], int current_row, int current_column, size_t word_len); // Checks if the `word` matches the `TARGET` from the current spot to the diagonal bottom right.

int main(int argc, char *argv[])
{
    FILE *file = fopen(FILE_PATH, "r");

    const size_t TARGET_LEN = strlen(TARGET);

    size_t row_len, row_count;
    row_len = row_count = TARGET_LEN; // At least as long as the target
    char **rows = NULL;
    rows = malloc(row_count * sizeof(char *)); // each item in the array is a pointer to a row
    assert(rows != NULL && "Not enough memory to `malloc` an array of rows of `char`s!");

    for (int r = 0; r < row_count; r++)
    {
        if (r >= row_count - 1)
        {
            rows = realloc(rows, (row_count * sizeof(char *)) * 2);
            assert(rows != NULL && "Not enough memory to `realloc` an array of rows of `char`s!");
            row_count *= 2;
        }

        rows[r] = malloc(row_len * sizeof(char));
        assert(rows[r] != NULL && "Not enough memory to `malloc` a row of `char`s!");

        if (row_filler(&(rows[r]), file, &row_len) == EOF)
        {
            row_count = r;
            free(rows[r]); // current row is getting wasted otherwise
            break;
        }

        printf("Row #: %d\tLength: %d\tContent: ", r, (int)row_len);
        row_printer(rows[r], row_len);
    }

    int target_freq = 0;
    target_freq = word_checker(rows, TARGET_LEN, row_len, row_count);
    printf("Total occurences of \"%s\": %d\n", TARGET, target_freq);

    fclose(file);
    for (int r = 0; r < row_count; r++)
        free(rows[r]);
    free(rows);

    return EXIT_SUCCESS;
}

int unixgetchar(FILE *file)
{
    int c;

    while ((c = fgetc(file)) == '\r')
    {
        ; // Empty loop body skips any '\r' characters
    }

    return c;
}

char *str_reverse(char word[], size_t str_len)
{
    for (int i = 0; i < str_len / 2; i++)
    {
        char temp = word[i];

        // -1 as well to not replace/copy the '\0'
        word[i] = word[str_len - 1 - i];
        word[str_len - 1 - i] = temp;
    }

    return word;
}

int row_filler(char *row[], FILE *file, size_t *row_len) // pointer to row[] so contents from realloc retained when function exits
{
    static bool filled_once = false;

    char c;
    for (size_t i = 0; i < *row_len; i++)
    {
        c = unixgetchar(file);

        if (c == ROW_END || c == EOF)
        {
            if (!filled_once)
                filled_once = true;

            *row_len = (i == 0) ? *row_len : i; // only update value of row_len if EOF isn't at the start of reading row
            return c;                           // assuming that `ROW_END != EOF`.
        }

        if (i >= *row_len - 1 && !filled_once) // resize, if necessary (nearing the end of `row_len` and still have more to read in)
        {
            *row = realloc(*row, *row_len * 2);
            assert(*row != NULL && "Not enough memory to `realloc` a row of `char`s!");
            *row_len *= 2;
        }

        (*row)[i] = c;
    }

    if (filled_once)
        unixgetchar(file); // Get rid of the trailing '\n' so it doesn't interfere with the next iteration

    return c; // assuming that `ROW_END != EOF`.
}

void row_printer(char row[], size_t row_len)
{
    for (int i = 0; i < row_len; i++)
    {
        printf("%c", row[i]);
    }
    printf("\n");
}

int word_checker(char **rows, size_t word_len, size_t row_len, size_t row_count)
{
    int frequency = 0;
    char word[word_len + 1];               // +1 for the '\0'
    for (int i = 0; i < word_len + 1; i++) // +1 to cover the final '\0' too
        word[i] = '\0';                    // Initialise all to empty so stopping works properly

    for (int r = 0; r < row_count; r++)
    {
        char *row = rows[r];

        for (int c = 0; c < row_len; c++)
        {
            // horizontal filling first
            if (c <= row_len - word_len)                                      // Don't go out of bounds
                frequency += horizontal_word_checker(word, row, c, word_len); // straight ahead

            // vertical filling next
            if (r <= row_count - word_len)
            {
                frequency += vertical_word_checker(word, rows, r, c, word_len); // straight down

                // diagonally - top to bottom left
                if (c >= word_len - 1) // -1 because `c` is zero-indexed
                    frequency += diagonal_left_word_checker(word, rows, r, c, word_len);

                // diagonally - top to bottom right
                if (c <= row_len - word_len)
                    frequency += diagonal_right_word_checker(word, rows, r, c, word_len);
            }
        }
    }

    return frequency;
}

/*
********************************************************************************************
     any bounds checking must have happened before coming into the following functions.
********************************************************************************************
*/

int word_validator(char word[], size_t word_len)
{
    return ((strncmp(word, TARGET, word_len) == 0) +
            (strncmp(str_reverse(word, word_len), TARGET, word_len) == 0));
}

int horizontal_word_checker(char word[], char row[], int offset, size_t word_len)
{
    strncpy(word, row + offset, word_len); // copy row[c:...] -> word

    return word_validator(word, word_len);
}

int vertical_word_checker(char word[], char *rows[], int current_row, int current_column, size_t word_len)
{
    // straight down
    for (int i = 0; i < word_len; i++)
        word[i] = rows[current_row + i][current_column];

    return word_validator(word, word_len);
}

int diagonal_left_word_checker(char word[], char *rows[], int current_row, int current_column, size_t word_len)
{
    for (int i = 0; i < word_len; i++)
        word[i] = rows[current_row + i][current_column - i];

    return word_validator(word, word_len);
}

int diagonal_right_word_checker(char word[], char *rows[], int current_row, int current_column, size_t word_len)
{
    for (int i = 0; i < word_len; i++)
        word[i] = rows[current_row + i][current_column + i];

    return word_validator(word, word_len);
}
