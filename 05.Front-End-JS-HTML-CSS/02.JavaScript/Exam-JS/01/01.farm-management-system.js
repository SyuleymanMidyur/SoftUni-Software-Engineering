function manageFarm(input) {
    const n = parseInt(input.shift());
    const farmers = {};

    for (let i = 0; i < n; i++) {
        const [name, area, tasks] = input.shift().split(' ');
        farmers[name] = {
            area: area,
            tasks: tasks.split(',').sort()
        };
    }

    while (input.length > 0) {
        const command = input.shift();
        if (command === "End") break;

        const [action, farmerName, ...args] = command.split(' / ');

        if (action === "Execute") {
            const [workArea, task] = args;
            if (farmers[farmerName].area === workArea && farmers[farmerName].tasks.includes(task)) {
                console.log(`${farmerName} has executed the task: ${task}!`);
            } else {
                console.log(`${farmerName} cannot execute the task: ${task}.`);
            }

        } else if (action === "Change Area") {
            const [newArea] = args;
            farmers[farmerName].area = newArea;
            console.log(`${farmerName} has changed their work area to: ${newArea}`);

        } else if (action === "Learn Task") {
            const [newTask] = args;
            if (farmers[farmerName].tasks.includes(newTask)) {
                console.log(`${farmerName} already knows how to perform ${newTask}.`);

            } else {
                farmers[farmerName].tasks.push(newTask);
                farmers[farmerName].tasks.sort();
                console.log(`${farmerName} has learned a new task: ${newTask}.`);
            }
        }
    }

    // Print final results
    for (const [name, data] of Object.entries(farmers)) {
        console.log(`Farmer: ${name}, Area: ${data.area}, Tasks: ${data.tasks.join(', ')}`);
    }
}

// Example

manageFarm([
    "3",
    "Alex apiary harvesting,honeycomb",
    "Emma barn milking,cleaning",
    "Chris garden planting,weeding",
    "Execute / Alex / apiary / harvesting",
    "Learn Task / Alex / beeswax",
    "Execute / Alex / apiary / beeswax",
    "Change Area / Emma / apiary",
    "Execute / Emma / apiary / milking",
    "Execute / Chris / garden / watering",
    "Learn Task / Chris / pruning",
    "Execute / Chris / garden / pruning",
    "End"
    ]);