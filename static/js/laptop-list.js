/* จัดการรายการแล็ปท็อปฝั่ง client: กรองแบบ realtime + เรียงลำดับราคาแบบ realtime
   ใช้ data attributes ของ .laptop-item (data-brand / data-price / data-ram / data-hdd)
   ทำงานเฉพาะรายการที่แสดงอยู่บนหน้านั้น ไม่มีการโหลดหน้าใหม่ */
(function () {
    var itemsContainer = document.getElementById('laptop-items');
    var items = itemsContainer
        ? Array.prototype.slice.call(itemsContainer.querySelectorAll('.laptop-item'))
        : [];

    // จำลำดับตั้งต้นไว้สำหรับตัวเลือก "ค่าตั้งต้น"
    items.forEach(function (item, i) { item.dataset.index = i; });

    // ทาสีสลับแถว (ลายเดิมของเว็บ) ใหม่ตามรายการที่มองเห็นอยู่
    function restripe() {
        var visible = items
            .filter(function (item) { return item.style.display !== 'none'; })
            .sort(function (a, b) {
                return (a.compareDocumentPosition(b) & Node.DOCUMENT_POSITION_FOLLOWING) ? -1 : 1;
            });
        visible.forEach(function (item, i) {
            var card = item.querySelector('.laptop-card');
            if (!card) return;
            card.style.background = (i % 2 === 1) ? '#efeded' : '#fff';
            card.style.color = (i % 2 === 1) ? '#fff' : '#efeded';
        });
    }

    // ---------- เรียงลำดับราคา ----------
    window.sortLaptopList = function (mode) {
        if (!items.length) return;
        var order = items.slice();
        if (mode === 'lowsort') {
            order.sort(function (a, b) { return a.dataset.price - b.dataset.price; });
        } else if (mode === 'expensivesort') {
            order.sort(function (a, b) { return b.dataset.price - a.dataset.price; });
        } else {
            order.sort(function (a, b) { return a.dataset.index - b.dataset.index; });
        }
        order.forEach(function (item) { itemsContainer.appendChild(item); });
        restripe();
    };

    // ---------- กรองข้อมูล ----------
    var panel = document.getElementById('filter-panel');
    if (panel && items.length) {
        var checkedValues = function (name) {
            var boxes = panel.querySelectorAll('input[name="' + name + '"]:checked');
            return Array.prototype.map.call(boxes, function (box) { return box.value; });
        };

        var parsePrice = function (name) {
            var raw = panel.querySelector('input[name="' + name + '"]').value.replace(/,/g, '').trim();
            var value = parseFloat(raw);
            return isNaN(value) ? null : value;
        };

        var applyFilter = function () {
            var brands = checkedValues('brand');
            var rams = checkedValues('ram');
            var hdds = checkedValues('hdd_capacity');
            var minPrice = parsePrice('min_price');
            var maxPrice = parsePrice('max_price');

            var visibleCount = 0;
            items.forEach(function (item) {
                var price = parseFloat(item.dataset.price);
                var show =
                    (brands.length === 0 || brands.indexOf(item.dataset.brand) !== -1) &&
                    (rams.length === 0 || rams.indexOf(item.dataset.ram) !== -1) &&
                    (hdds.length === 0 || hdds.indexOf(item.dataset.hdd) !== -1) &&
                    (minPrice === null || price >= minPrice) &&
                    (maxPrice === null || price <= maxPrice);
                item.style.display = show ? 'flex' : 'none';
                if (show) visibleCount++;
            });

            var emptyMessage = document.getElementById('no-filter-match');
            if (emptyMessage) {
                emptyMessage.style.display = (visibleCount === 0) ? 'block' : 'none';
            }
            restripe();
        };

        Array.prototype.forEach.call(
            panel.querySelectorAll('input[type="checkbox"]'),
            function (box) { box.addEventListener('change', applyFilter); }
        );
        Array.prototype.forEach.call(
            panel.querySelectorAll('input[name="min_price"], input[name="max_price"]'),
            function (input) { input.addEventListener('input', applyFilter); }
        );
    }
})();
