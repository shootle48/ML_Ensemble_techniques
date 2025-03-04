document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");
  const resetBtn = document.getElementById("reset-btn");
  const toggleTableBtn = document.getElementById("toggle-table-btn");
  const tableContainer = document.getElementById("table-container");
  const dataTable = document.querySelector(".dataframe"); // ดึงตารางที่ Flask เรนเดอร์มา

  // ตรวจสอบการกรอกข้อมูลก่อนส่งฟอร์ม
  form.addEventListener("submit", function (event) {
    const inputs = form.querySelectorAll('input[type="text"]');
    let valid = true;
    inputs.forEach(function (input) {
      if (input.value.trim() === "") {
        valid = false;
        input.style.border = "1px solid #ff5252";
      } else {
        input.style.border = "none";
      }
    });

    if (!valid) {
      event.preventDefault();
      alert("กรุณากรอกข้อมูลให้ครบถ้วน");
    }
  });

  // ปุ่มล้างค่าฟอร์ม
  resetBtn.addEventListener("click", function () {
    document.getElementById("Glucose").value = "";
    document.getElementById("Insulin").value = "";
    document.getElementById("BMI").value = "";
  });

  // แสดง/ซ่อนตาราง
  toggleTableBtn.addEventListener("click", function () {
    if (tableContainer.style.display === "none") {
      tableContainer.style.display = "block";
      toggleTableBtn.textContent = "ซ่อนข้อมูลตาราง";
    } else {
      tableContainer.style.display = "none";
      toggleTableBtn.textContent = "แสดงข้อมูลตาราง";
    }
  });

  // เลือกข้อมูลจากตารางไปเติมลงในฟอร์ม
  if (dataTable) {
    dataTable.addEventListener("click", function (event) {
      const row = event.target.closest("tr");
      if (row) {
        const cells = row.getElementsByTagName("td");
        if (cells.length >= 3) {
          document.getElementById("Glucose").value = cells[1].textContent;
          document.getElementById("Insulin").value = cells[4].textContent;
          document.getElementById("BMI").value = cells[5].textContent;
        }
      }
    });
  }
});
