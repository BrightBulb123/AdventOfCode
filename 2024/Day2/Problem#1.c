#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <assert.h>

#define FILE_PATH "Day2Input.txt"
#define TEST_FILE_PATH "Day2TestInput.txt"

#define DATA_SEP ' ' // Separator of integers in the input file(s).
#define LEAST_DIFF 1
#define MOST_DIFF 3

int unixgetchar(FILE *file);                            // Only returns a '\n' instead of '\r\n', otherwise the same as `getchar()`.
int intgetter(FILE *file, bool *end_of_report);         // Returns the next integer read in from a file, else, if EOF encountered, returns EOF; if '\n' (end of report), sets `end_of_report` to `true`.
int rep_getter(FILE *file, int *report[], int rep_len); // Returns the length of the `report` read in, and also populates the `report` from the `file`. Returns an EOF if EOF is encountered in `file`.
int safe_reps_counter(FILE *file);                      // Returns the number of "safe" reports in the `file` provided.
bool is_rep_safe(int report[], int rep_len);            // Checks if the current `report` passed in is "safe", and returns `true` if it is

int main(int argc, char *argv[])
{
    FILE *file = fopen(FILE_PATH, "r");
    
    int safe_rep_count = safe_reps_counter(file);

    printf("Total safe reports in file: %d\n", safe_rep_count);

    fclose(file);
    file = NULL;

    return EXIT_SUCCESS;
}

int unixgetchar(FILE *file)
{
    int c;

    while ((c = fgetc(file)) == '\r')
    {
        ; // Empty loop skips the '\r'
    }

    return c;
}

int intgetter(FILE *file, bool *end_of_report)
{
    int i, c, c_len = 1, digits = 0;

    char *c_repr = NULL;
    c_repr = malloc(sizeof(char) * c_len); // Start with just a string of length one,
    assert(c_repr != NULL && "Not enough memory to allocate `c_repr`!");

    c_repr[0] = '\0'; // String starts with null byte, just in-case nothing read in, so `atoi` doesn't parse garbage

    while ((c = unixgetchar(file)) != EOF)
    {
        if (c == DATA_SEP) // Whitespace encountered
        {
            if (digits == 0) // Nothing read in yet, keep going till some data
                continue;
            else // already read some data, exit for this iteration
                break;
        }
        else if (c == '\n')
        {
            if (digits == 0)
                return '\n';
            else
            {
                *end_of_report = true;
                break;
            }
        }

        digits++; // A digit *was* read in, it wasn't just a whitespace character
        if (digits >= c_len)
        {
            c_repr = realloc(c_repr, sizeof(char) * (2 * c_len)); // double the char array in size
            assert(c_repr != NULL && "Not enough memory to reallocate `c_repr`!");
            c_len *= 2;
        }

        c_repr[digits - 1] = (char)c;
        c_repr[digits] = '\0'; // Terminate the string
    }

    if (c == EOF && digits == 0) // Nothing was read in, file stream ended
        return EOF;

    i = atoi(c_repr);

    free(c_repr);
    c_repr = NULL;

    return i;
}

int rep_getter(FILE *file, int *report[], int rep_len)
{
    bool end_of_report = false;
    int n, count_ints = 0;
    while ((n = intgetter(file, &end_of_report)) != EOF)
    {
        if (count_ints >= rep_len)
        {
            *report = realloc(*report, sizeof(int) * (2 * rep_len)); // Double the report array size if needed
            assert(*report != NULL && "Not enough memory to reallocate `report`!");
            rep_len *= 2;
        }

        (*report)[count_ints++] = n;

        if (end_of_report)
            break;
    }

    if (n == EOF)
        return EOF;

    return count_ints;
}

int safe_reps_counter(FILE *file)
{
    int total = 0, rep_len = 1, *report = NULL;
    report = malloc(sizeof(int) * rep_len);
    assert(report != NULL && "Not enough memory to allocate `report`!");

    do
    {
        rep_len = rep_getter(file, &report, rep_len);
        bool safe = is_rep_safe(report, rep_len);

        if (safe)
            total++;
    } while (rep_len != EOF);

    free(report);
    report = NULL;

    return total;
}

bool is_rep_safe(int report[], int rep_len)
{
    bool safe = true;
    bool increasing = true, decreasing = true;

    for (int i = 1; i < rep_len; i++)
    {
        int diff = report[i] - report[i - 1];

        if (diff == 0)
            return (safe = false); // Unsafe, no change detected
        else if (diff > 0)
        {
            if (!increasing)
                return (safe = false); // Change in gradient

            increasing = true;
            decreasing = false;
        }
        else if (diff < 0)
        {
            if (!decreasing)
                return (safe = false); // Change in gradient

            decreasing = true;
            increasing = false;
        }

        if (abs(diff) < LEAST_DIFF || abs(diff) > MOST_DIFF)
            return (safe = false); // Too big or little of a change
    }

    return safe;
}
