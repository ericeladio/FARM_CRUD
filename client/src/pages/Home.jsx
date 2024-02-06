import { useEffect, useState} from "react"
import axios from "axios"

function Home() {

  const [tasks, setTasks] = useState([])

   useEffect(() => {
    async function fetchTasks() {
      const res = await axios.get('http://localhost:8000/api/tasks')
      setTasks(res.data)
      console.log(res.data)
    }
    fetchTasks()  
  },[])
  return (
    <>
      <h1 className='text-3xl font-bolddd'>Home</h1>
      {tasks.map((task) => (
        <div key={task.id}>
          <h1>{task.title}</h1>
          <p>{task.description}</p>
        </div>
      ))}
    </>
  )
}

export default Home