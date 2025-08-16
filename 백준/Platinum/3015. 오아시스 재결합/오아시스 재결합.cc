#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<int> arr(N);
    for (int i = 0; i < N; i++) cin >> arr[i];

    stack<pair<int,int>> st;
    long long ans = 0;

    for (int i = 0; i < N; i++) {
        int h = arr[i];

        while (!st.empty() && st.top().first < h) {
            ans += st.top().second;
            st.pop();
        }

        if (st.empty()) {
            st.push({h, 1});
        } else if (st.top().first == h) {
            ans += st.top().second;
            st.top().second += 1;
            if (st.size() > 1) ans += 1;
        } else { 
            ans += 1;
            st.push({h, 1});
        }
    }

    cout << ans;
    return 0;
}
