"""
Design a food rating system that can do the following:
Modify the rating of a food item listed in the system.
Return the highest-rated food item for a type of cuisine in the system.
Implement the FoodRatings class:
FoodRatings(String[] foods, String[] cuisines, int[] ratings) Initializes the system. The food
items are described by foods, cuisines and ratings, all of which have a length of n.
foods[i] is the name of the ith food,
cuisines[i] is the type of cuisine of the ith food, and
ratings[i] is the initial rating of the ith food.
void changeRating(String food, int newRating) Changes the rating of the food item with the name
food.
String highestRated(String cuisine) Returns the name of the food item that has the highest
rating for the given type of cuisine. If there is a tie, return the item with the
lexicographically smaller name.
Note that a string x is lexicographically smaller than string y if x comes before y in
dictionary order, that is, either x is a prefix of y, or if i is the first position such that
x[i] != y[i], then x[i] comes before y[i] in alphabetic order.

Example 1:
Input
["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating",
"highestRated"]
[[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese",
"japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"],
["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]
Output
[null, "kimchi", "ramen", null, "sushi", null, "ramen"]
Explanation
FoodRatings foodRatings = new FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen",
"bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15,
14, 7]);
foodRatings.highestRated("korean"); // return "kimchi"
                                    // "kimchi" is the highest rated korean food with a rating
of 9.
foodRatings.highestRated("japanese"); // return "ramen"
                                      // "ramen" is the highest rated japanese food with a
rating of 14.
foodRatings.changeRating("sushi", 16); // "sushi" now has a rating of 16.
foodRatings.highestRated("japanese"); // return "sushi"
                                      // "sushi" is the highest rated japanese food with a
rating of 16.
foodRatings.changeRating("ramen", 16); // "ramen" now has a rating of 16.
foodRatings.highestRated("japanese"); // return "ramen"
                                      // Both "sushi" and "ramen" have a rating of 16.
                                      // However, "ramen" is lexicographically smaller than
"sushi".

Constraints:
1 <= n <= 2 * 104
n == foods.length == cuisines.length == ratings.length
1 <= foods[i].length, cuisines[i].length <= 10
foods[i], cuisines[i] consist of lowercase English letters.
1 <= ratings[i] <= 108
All the strings in foods are distinct.
food will be the name of a food item in the system across all calls to changeRating.
cuisine will be a type of cuisine of at least one food item in the system across all calls to
highestRated.
At most 2 * 104 calls in total will be made to changeRating and highestRated.
"""

from typing import List
from sortedcontainers import SortedSet


# ********** TLE ***********

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        food_map = {}
        ss_map = {}
        for i in range(len(foods)):
            food_map[foods[i]] = [-ratings[i], cuisines[i]]
            ss_map[cuisines[i]] = ss_map.get(cuisines[i], SortedSet()) | [(-ratings[i], foods[i])]
        self.food_map = food_map
        self.ss_map = ss_map

    def changeRating(self, food: str, newRating: int) -> None:
        oldRating, cuisine = self.food_map[food]
        self.ss_map[cuisine].remove((oldRating, food))
        self.ss_map[cuisine].add((-newRating, food))
        self.food_map[food][0] = -newRating

    def highestRated(self, cuisine: str) -> str:
        return self.ss_map[cuisine][0][1]


if __name__ == "__main__":
    # Your FoodRatings object will be instantiated and called as such:
    # obj.changeRating(food, newRating)
    # param_2 = obj.highestRated(cuisine)

    # case_1
    _foods = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]
    _cuisines = ["korean", "japanese", "japanese", "greek", "japanese", "korean"]
    _ratings = [9, 12, 8, 15, 14, 7]
    obj = FoodRatings(_foods, _cuisines, _ratings)

    assert obj.highestRated("korean") == "kimchi"
    assert obj.highestRated("japanese") == "ramen"
    assert obj.changeRating("sushi", 16) is None
    assert obj.highestRated("japanese") == "sushi"
    assert obj.changeRating("ramen", 16) is None
    assert obj.highestRated("japanese") == "ramen"

    # case_2
    obj2 = FoodRatings(["biihw"], ["okxsrcqn"], [13])

    assert obj2.changeRating("biihw", 9) is None
    assert obj2.changeRating("biihw", 6) is None

    # case_3
    obj3 = FoodRatings(["emgqdbo", "jmvfxjohq", "qnvseohnoe", "yhptazyko", "ocqmvmwjq"],
                       ["snaxol", "snaxol", "snaxol", "fajbervsj", "fajbervsj"],
                       [2, 6, 18, 6, 5])

    assert obj3.changeRating("qnvseohnoe", 11) is None
    assert obj3.highestRated("fajbervsj") == "yhptazyko"
    assert obj3.changeRating("emgqdbo", 3) is None
    assert obj3.changeRating("jmvfxjohq", 9) is None
    assert obj3.changeRating("emgqdbo", 14) is None
    assert obj3.highestRated("fajbervsj") == "yhptazyko"
    assert obj3.highestRated("snaxol") == "emgqdbo"