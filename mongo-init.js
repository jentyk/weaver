const fs = require('fs');

try {
    // The file is small, so I can process it in memory.
    const data = fs.readFileSync('/tmp/employees.csv', 'utf8').split("\n");
    let header = data.shift().split(",")
    let employeeData = data.map(
        (e) => Object.fromEntries(e.split(",").map((e, i) => [header[i], e.trim()])));
    db.employees.insertMany(employeeData)
} catch (err) {
    console.error(err);
}
