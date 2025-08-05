#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    const int MAX = 100001;
    vector<int> dist(MAX, 1e9);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;

    dist[n] = 0;
    pq.push({0, n});

    while (!pq.empty()) {
        auto [time, cur] = pq.top();
        pq.pop();

        if (cur == k) {
            cout << time << '\n';
            return 0;
        }

        if (cur * 2 < MAX && dist[cur * 2] > time) {
            dist[cur * 2] = time;
            pq.push({time, cur * 2});
        }
        if (cur + 1 < MAX && dist[cur + 1] > time + 1) {
            dist[cur + 1] = time + 1;
            pq.push({time + 1, cur + 1});
        }
        if (cur - 1 >= 0 && dist[cur - 1] > time + 1) {
            dist[cur - 1] = time + 1;
            pq.push({time + 1, cur - 1});
        }
    }

    return 0;
}
