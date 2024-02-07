import { useEffect, useState} from "react"
import TaksList from "../components/TaksList"
import { getAllTasks } from "../api/tasks"

function Home() {

  const [tasks, setTasks] = useState([])

   useEffect(() => {
    async function fetchTasks() {
      const res = await getAllTasks()
      setTasks(res.data)
      console.log(res.data)
    }
    fetchTasks()  
  },[])
  return (
      <TaksList tasks={tasks} />
  )
}

export default Home