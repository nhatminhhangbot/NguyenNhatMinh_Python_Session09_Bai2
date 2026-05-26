# Phần tử "GE100-FAST" được chèn vào vị trí đầu tiên (index 0). Tất cả các phần tử đứng sau nó bị đẩy lùi sang phải 1 vị trí
# Sau khi chèn "GE100-FAST" vào đầu, "GE102-WRONG" chuyển từ index 1 sang index 2 nên lệnh cập nhật ghi đè lên "GE101" lúc này ở index 1
# Dòng express_orders.pop(3) không xóa đúng đơn hàng bị hủy vì sự dịch chuyển index ở bước cập nhật
# Nếu muốn xóa đúng đơn hàng "GE103-CANCEL", nên dùng: express_orders.remove("GE103-CANCEL")
# pop() không truyền index sẽ mặc định lấy và xóa phần tử cuối cùng của danh sách nên lệnh sẽ lấy ra đơn cuối cùng ("GE104") thay vì đơn đầu tiên
# Muốn lấy đơn hàng đầu tiên trong danh sách ra để giao, cần viết: current_order = express_orders.pop(0)
# Code đúng:

express_orders = ["GE101", "GE102-WRONG", "GE103-CANCEL"]

express_orders.append("GE104")

express_orders.insert(0, "GE100-FAST")

express_orders[2] = "GE102-UPDATED"

express_orders.remove("GE103-CANCEL")

current_order = express_orders.pop(0)

print("Danh sách đơn hàng còn lại:", express_orders)
print("Đơn hàng đang giao:", current_order)