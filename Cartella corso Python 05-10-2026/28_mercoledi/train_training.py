from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

X, y = make_moons(n_samples=400, noise=0.35, random_state=42)    # dati con molto rumore
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

for k in [1, 15]:
    knn = KNeighborsClassifier(n_neighbors=k).fit(X_train, y_train)
    print(f"k={k:2d}  training: {knn.score(X_train, y_train):.2f}"   # punteggio sui dati visti
          f"  test: {knn.score(X_test, y_test):.2f}")   









#============================================================================================

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

X, y = load_breast_cancer(return_X_y=True)

# 1° split: 80% (train+validation) / 20% test
X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# 2° split: dal restante 80%, il 25% va in validation -> 60/20/20 sul totale
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.25, random_state=42)

migliore_k, migliore_val = None, 0
for k in range(1, 31, 2):                                   # k dispari da 1 a 29
    knn = KNeighborsClassifier(n_neighbors=k).fit(X_train, y_train)
    val = knn.score(X_val, y_val)                           # la scelta si fa sul VALIDATION
    if val > migliore_val:
        migliore_k, migliore_val = k, val

finale = KNeighborsClassifier(n_neighbors=migliore_k).fit(X_train, y_train)
print("k scelto:", migliore_k, "| validation:", round(migliore_val, 3))
print("Stima finale sul test:", round(finale.score(X_test, y_test), 3))   # test usato UNA volta