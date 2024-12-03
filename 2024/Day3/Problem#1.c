#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
#include <assert.h>

#define FILE_PATH "Day3Input.txt"
#define TEST_FILE_PATH "Day3TestInput.txt"

#define OP_NAME "mul" // Operation name
#define NUM_SEP ','   // Number argument separation character
#define MIN_NUM_LEN 1 // Minimum digits in a number
#define MAX_NUM_LEN 3 // Maximum digits in a number
#define NUM_COUNT 2   // How many numbers there should be

int unixgetchar(FILE *file);                                                                    // Returns only '\n' compared to '\r\n' for NT platforms, otherwise functionally the same as `fgetc(file)`.
int strshifter(FILE *file, char str[], size_t size);                                            // Shifts the entire string by one to the left, adding in a new character read in from `file` at the end.
bool strvaliditychecker(char str[], size_t min_size, size_t max_size, size_t size, int nums[]); // Returns if the given `str` is valid or not, as well as filling up the `nums` array with the actual numbers from the `str` in the cade of a valid `str`.

int main(int argc, char *argv[])
{
    FILE *file = fopen(FILE_PATH, "r");

    // 2 for the brackets, 1 for NUM_SEP
    const size_t min_size = strlen(OP_NAME) + (NUM_COUNT * MIN_NUM_LEN) + 2 + 1;
    const size_t max_size = strlen(OP_NAME) + (NUM_COUNT * MAX_NUM_LEN) + 2 + 1;

    char str[max_size + 1]; // +1 for actual '\0'
    for (int i = 0; i < max_size + 1; i++)
    {
        str[i] = '\0';
    }

    int total_prod = 0;
    int nums[NUM_COUNT];

    while (strshifter(file, str, max_size + 1) != EOF)
    {
        bool valid = strvaliditychecker(str, min_size, max_size, max_size, nums);
        if (valid)
        {
            int sum = 1;
            for (int i = 0; i < NUM_COUNT; i++)
            {
                sum *= nums[i];
            }

            total_prod += sum;
        }
    }

    printf("Total: %d\n", total_prod);

    fclose(file);
    file = NULL;

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

int strshifter(FILE *file, char str[], size_t size)
{
    char c = unixgetchar(file);

    if (c == EOF)
    {
        if (strnlen(str, size) == 0)
            return EOF;
        else
            c = '\0'; // Fill string with null bytes
    }

    for (int i = 1; i < size - 1; i++)
    {
        str[i - 1] = str[i];
    }

    str[size - 2] = c; // Keep the last item the '\0', and replace the last actual character (size is not zero indexed, so -1 for that too)

    return (!(EOF)); // return valid number, signifying file is valid
}

bool strvaliditychecker(char str[], size_t min_size, size_t max_size, size_t size, int nums[])
{
    bool valid = true;
    int pos = 0;

    int len = strnlen(str, size);
    if (len < min_size || len > max_size)
        return (valid = false);

    pos += strlen(OP_NAME);
    if (strncmp(str, OP_NAME, pos) != 0)
        return (valid = false);

    if (str[pos] == '(')
        pos += 1;
    else
        return (valid = false);

    for (int n_count = 0; n_count < NUM_COUNT; n_count++)
    {
        int num_len = 0;
        for (int i = pos; i < size; i++)
        {
            char c = str[i];

            if (isdigit(c))
                num_len++;
            else if ((c == NUM_SEP && n_count != NUM_COUNT - 1) || (c == ')' && n_count == NUM_COUNT - 1)) // Which separator to pick
            {
                char num[num_len + 1]; // Full number read in, convert to int now, +1 for '\0'
                for (int j = 0; j < num_len; j++)
                    num[j] = str[pos + j];
                num[num_len] = '\0';
                nums[n_count] = atoi(num);

                pos += num_len + 1; // +1 for separator (either NUM_SEP or ')')
                break;              // Stop checking the numbers now.
            }
            else // Not a number, and not a valid separator either
                return (valid = false);
        }

        if (num_len < MIN_NUM_LEN || num_len > MAX_NUM_LEN)
            return (valid = false);
    }

    return valid;
}
