# Hàm sinh
1. [Cú pháp](#introduction)
2. Phân Hoạch số nguyên
3. Hàm sinh mũ
4. Toán tử tổng
## 1. Cú pháp <a name="introduction"></a>
Dùng thư viện sympy của python
`from sympy import`
Các biểu thức
```
expr.doit() :Thực hiện tính toán biểu thức
expr.simplify() :Rút gọn biểu thức
expr.cancel() : Rút gọn phân số
expr.expand() : Rút gọn đa thức
expr.factor() : Phân tích biểu thức thành thừa số
expr.subs(X, y) : Thay biểu thức con X thành y
expr.diff() : Đạo hàm theo 1 biến duy nhất
expr.diff(x) : Đạo hàm theo biến x
expr.diff(x, 5): Đạo hàm cấp 5
expr.series(x, X, 5): Khai triển Taylor của biểu thức theo biến x, tâm tại X, tới cấp 4
Sum(expr, (i, a, b)): Tính tổng từ a tới b
```
Các kí hiệu hay dùng
`binomial(n, r) : Tính tổ hợp`
### Định nghĩa
#### ĐN1: Hàm sinh có dạng a(i)*x**(i)
[VD: Xác định hệ số của x^15](XacDinhHeSo.ipynb)

