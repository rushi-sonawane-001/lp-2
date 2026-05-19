#include <iostream>
#include <queue>
#include <vector>
using namespace std;

struct Node
{
    int v, cost;

    bool operator<(const Node& p) const
    {
        return cost > p.cost;
    }
};

vector<pair<int,int>> g[5];
int h[5] = {7, 6, 2, 1, 0};

void astar(int start, int goal)
{
    priority_queue<Node> pq;
    bool visited[5] = {0};

    pq.push({start, h[start]});

    while(!pq.empty())
    {
        int u = pq.top().v;
        pq.pop();

        if(visited[u]) continue;

        visited[u] = true;

        cout << u << " ";

        if(u == goal)
        {
            cout << "\nGoal Reached";
            return;
        }

        for(auto x : g[u])
            if(!visited[x.first])
                pq.push({x.first, x.second + h[x.first]});
    }
}

int main()
{
    g[0] = {{1,1},{2,4}};
    g[1] = {{3,2}};
    g[2] = {{3,1}};
    g[3] = {{4,3}};

    cout << "A* Path: ";
    astar(0,4);
}