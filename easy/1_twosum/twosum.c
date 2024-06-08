/*Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
*/

#include <stdio.h>
#include <stdlib.h>


int *twoSum_brute( const int *nums, int target){

    int length = sizeof(nums) / sizeof(nums[0]);
    int *result = (int *)malloc(2 * sizeof(int));
    for (int index = 0; index < length; index++){
        for (int j = index + 1; j <length; j++){
            if (nums[index] + nums[j] == target){
                result[0] = index;
                result[1] = j;
                return result;
            }
        }
    }

    return NULL;
}

// Define a hash table entry
typedef struct {
    int key;
    int value;

} HashTableEntry;

// Define the hash table
typedef struct {
    HashTableEntry *entries;
    int size;
} HashTable;

// Create a hash table
HashTable* createHashTable(int size){
    HashTable *table = (HashTable *)malloc(sizeof(HashTable));
    table->entries = (HashTableEntry *)malloc(sizeof(HashTableEntry) * size);
    table->size = size;

    for (int index = 0; index < size; index++){
        table->entries[index].key = -1; // Initialize keys to -1 indicating emtpy
    }
    return table;
}

// Hash function 
int hash(int key, int size){

    return abs(key) % size;
}

// Insert into hash table
void insert(HashTable *table, int key, int value){
    int index = hash(key, table->size);

    while (table->entries[index].key != -1){
        index = (index + 1) % table->size;
    }

    table->entries[index].key = key;
    table->entries[index].value = value;
}

// find the index of the complement
int findIndex(HashTable *table, int key){
    int index = hash(key, table->size);
    while(table->entries[index].key != -1){
        if(table->entries[index].key == key){
            return table->entries[index].value;
        }

        index = (index + 1) % table->size;
    }
    return -1;
}

// Free the hash table
void freeHashTable(HashTable *table){
    if (table == NULL){
        return;
    }
    free(table->entries);
    free(table);
}
// None brute force solution
int *twoSum_non_brute( const int *nums, int target){
    int length = sizeof(nums) / sizeof(nums[0]);
    int hashTableSize =  length * 2;
    HashTable *table = createHashTable(hashTableSize);

    int *result = (int *)malloc(2 * sizeof(int));

    for (int index = 0; index < length; index++){
        int complement = target - nums[index];
        int complementIndex = findIndex(table, complement);
        if (complementIndex != -1){
            result[0] = complementIndex;
     
            result[1] = index;
            freeHashTable(table);
            return result;
        }
        insert(table, nums[index], index);
    }

    freeHashTable(table);
    return NULL;

}
int main(void){

    int nums[] = {2, 7, 11, 15};
    int target = 9;
   // int *result = twoSum_brute(nums, target);
    int *result = twoSum_non_brute(nums, target);
    if (result == NULL){
        printf("No solution found.\n");
    } else {
        printf("The two numbers are %d and %d.\n", result[0], result[1]);
        free(result);
    }
    return 0;
}


