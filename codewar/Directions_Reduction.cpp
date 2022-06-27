/*
Once upon a time, on a way through the old wild west,…

… a man was given directions to go from one point to another. 
The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too. 
Going to one direction and coming back the opposite direction is a needless effort. Since this is the wild west, 
with dreadfull weather and not much water, it's important to save yourself some energy, otherwise you might die of thirst!
How I crossed the desert the smart way.

The directions given to the man are, for example, the following (depending on the language):

["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
You can immediatly see that going "NORTH" and then "SOUTH" is not reasonable, 
better stay to the same place! So the task is to give to the man a simplified version of the plan. 
A better plan in this case is simply:
["WEST"]

Task

Write a function dirReduc which will take an array of strings and returns an array of strings 
with the needless directions removed (W<->E or S<->N side by side).
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <map>
#include <stack>
#include <iostream>
#include <algorithm>
using namespace std;

std::vector<std::string> dirReduc(std::vector<std::string> &arr)
{
    std::vector<std::string> ans;
    for (int i = 0; i < arr.size(); i++)
    {
        if (ans.empty())
        {
            ans.push_back(arr[i]);
        } else
        {
            if ((arr[i]=="NORTH" && ans.back()=="SOUTH") ||(arr[i]=="SOUTH" && ans.back()=="NORTH"))
            {
                ans.pop_back();
            } else if ((arr[i]=="WEST" && ans.back()=="EAST") ||(arr[i]=="EAST" && ans.back()=="WEST"))
            {
                ans.pop_back();
            } else
            {
                ans.push_back(arr[i]);
            }
            
        }        
    }
    
    return ans;
}

int main(){
    std::vector<std::string> path = {"NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"};
    std::vector<std::string> d=dirReduc(path);
    for (int i = 0; i < d.size(); i++)
    {
        cout<<d[i]<<endl;
    }
    
    return 0;
}