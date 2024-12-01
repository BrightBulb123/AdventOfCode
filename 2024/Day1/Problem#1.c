#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <assert.h>

// Assuming both files exist in the same directory
#define TEST_FILE_PATH "Day1TestInput.txt"
#define FILE_PATH "Day1Input.txt"

#define DATA_SEP ' ' // Separator between the two lists

typedef bool flag;

int unixgetchar(FILE *file);                                                    // Only returns '\n' in place of '\r\n' for NT-style line endings
int intgetter(FILE *file);                                                      // Returns the next integer encountered in the file stream (if EOF, then returns EOF)
int cmp_int(const void *a, const void *b);                                      // Comparison function for `qsort` for int array, returns 0 if a and b are equal, else returns >0 if a > b, and <0 if a < b.
int total_calc(int *left_list, int *right_list, int num_elems);                 // Calculates and returns the total distance between lists
int lists_filler(int **left_list, int **right_list, FILE *file, int list_size); // Fills up the two left and right lists passed in from the file, and returns the number of lines in the file (list length).

int main(int argc, char *argv[])
{
    FILE *file = fopen(FILE_PATH, "r");
    assert(file != NULL && "File not found!"); // Avoiding null pointer shenanigans

    int num_lines = 0;
    int list_size = 1;
    int *left_list = NULL, *right_list = NULL;

    num_lines = lists_filler(&left_list, &right_list, file, list_size);

    qsort(left_list, num_lines, sizeof(int), cmp_int);
    qsort(right_list, num_lines, sizeof(int), cmp_int);

    int total = total_calc(left_list, right_list, num_lines);

    printf("Total: %d\n", total);

    free(file);
    free(left_list);
    free(right_list);
    file = NULL;                   // FILE *
    left_list = right_list = NULL; // int *

    return EXIT_SUCCESS;
}

int unixgetchar(FILE *file)
{
    int c;
    while ((c = fgetc(file)) == '\r')
    {
        ; // Empty loop to bypass the '\r'
    }

    return c;
}

int intgetter(FILE *file)
{
    int i, c, c_len, digits_read;
    bool int_read = false;

    char *c_repr; // Character repr. of integer
    c_len = 1;    // start off with enough space for the null byte ('\0')

    c_repr = (char *)malloc(sizeof(int) * c_len);
    assert(c_repr != NULL && "Couldn't allocate enough memory for integer string representation!");
    c_repr[0] = '\0';

    digits_read = 0; // read in 0 digits to begin with
    while ((c = unixgetchar(file)) != EOF)
    {
        if ((c == DATA_SEP || c == '\n') && !int_read) // Keep reading if you've hit whitespace and haven't read something in yet.
            continue;
        else if ((c == DATA_SEP || c == '\n') && int_read) // Stop if you've hit whitespace and have already read something in.
            break;

        ++digits_read;
        if (digits_read >= c_len) // if we're gonna overflow the string
        {
            c_repr = (char *)realloc(c_repr, sizeof(int) * (2 * c_len)); // double the size of the array
            assert(c_repr != NULL && "Couldn't read in integer from file, not enough memory!");
            c_len *= 2;
        }

        c_repr[digits_read - 1] = c;
        c_repr[digits_read] = '\0';
        int_read = true;
    }

    if (c == EOF && !int_read)
        return EOF;

    i = atoi(c_repr);
    free(c_repr);
    c_repr = NULL;

    return i;
}

int cmp_int(const void *a, const void *b)
{
    return (*(int *)a) - (*(int *)b);
}

int total_calc(int *left_list, int *right_list, int num_elems)
{
    int total = 0;

    for (int i = 0; i < num_elems; i++)
    {
        total += abs(left_list[i] - right_list[i]);
    }

    return total;
}

int lists_filler(int **left_list, int **right_list, FILE *file, int list_size)
{
    // Have space for at least one integer in each list (assuming at least one line is supplied in the file)
    *left_list = (int *)malloc(sizeof(int) * list_size);
    *right_list = (int *)malloc(sizeof(int) * list_size);
    assert(*left_list != NULL && *right_list != NULL && "Not enough memory for a number list!");

    flag left = true; // start putting numbers in the left list first

    int i, num_lines;
    num_lines = 0;

    while ((i = intgetter(file)) != EOF)
    {
        if (num_lines >= list_size)
        {
            *left_list = (int *)realloc(*left_list, sizeof(int) * (2 * list_size));
            *right_list = (int *)realloc(*right_list, sizeof(int) * (2 * list_size));
            assert(*left_list != NULL && *right_list != NULL && "Not enough memory for a number list!");

            list_size *= 2;
        }

        if (left)
            (*left_list)[num_lines] = i;
        else
            (*right_list)[num_lines++] = i; // Increase number of lines after each right-hand side list iteration

        left = !left;
    }

    return num_lines;
}
