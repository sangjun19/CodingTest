#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> arr(n, 0), ans(n, -1), check(1000001, 0);
    stack<int> a;
    for(int i=0;i<n;i++) {
        cin >> arr[i];
        check[arr[i]] += 1;
    }    
    for(int i=n-1;i>=0;i--) {
        if(a.empty()) {
            ans[i] = -1;            
        }
        else {
            if(check[a.top()] > check[arr[i]]) {
                ans[i] = a.top();
            }
            else {
                while (!a.empty() && check[a.top()] <= check[arr[i]]) {
                    a.pop();
                }
                if(a.empty()) {
                    ans[i] = -1;
                }
                else {
                    ans[i] = a.top();
                }
            }
        }
        a.push(arr[i]);
        // if(!a.empty()) cout << a.top() << " ";
    }
    for(int i=0;i<n;i++) {
        cout << ans[i] << " ";
    }
    return 0;
}