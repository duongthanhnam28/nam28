# Lỗ hổng XSS
user_input = input("Nhập comment: ")
print("<div>" + user_input + "</div>")
