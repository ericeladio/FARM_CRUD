import TaskCard from "./TaskCard"

function TaksList({tasks}) {
  return (
    <div className="grid grid-cols-3 gap-4">
        {tasks.map((task) => (
        <TaskCard key={task._id} task={task} />
        ))}
    </div>
  )
}

export default TaksList