import { useState, useEffect } from "react"
import { useParams, useNavigate } from "react-router-dom"
import { getTask, createTask, editTask, deleteTask } from "../api/tasks"


function TaskForm() {

  const [title, setTitle] = useState('')
  const [description, setDescription] = useState('')
  const params = useParams()
  const navigate = useNavigate()
  
  const handleSubmit = async(e) => {
    e.preventDefault()
    // const res = await fetch('http://localhost:8000/api/tasks', {
    //   method: 'POST',
    //   body: JSON.stringify({
    //     title,
    //     description
    //   }),
    //   headers: {
    //     'Content-type': 'application/json'
    //   }

     try{
      if (params.id) {
        const res = await editTask(params.id,{title,description})
      }else{
        const res = await createTask({title,description})
      }
      navigate('/')
     }
     catch(err){
       console.log(err)
     }
    e.target.reset()

  }

  useEffect(() => {
    async function fetchTasks() {
      const res = await getTask(params.id)
      setTitle(res.data.title)
      setDescription(res.data.description)
    }
    if (params) {
      fetchTasks()
    }
  },[])


  return (
    <div className="flex items-center justify-center h-[calc(100vh-10rem)">
      <div>
      <form className="bgzinc-950 p-10"
        onSubmit={handleSubmit}
      >
        <h2
        className="text-3xl font-bold my-4"
        >
          {params.id ? 'Update Task' : 'Create Task'}
        </h2>
        <input type="text" placeholder="title"
        className="block py-2 px-3 mb-4  w-full   text-black"
        onChange={(e) => setTitle(e.target.value)}
        value={title}
        autoFocus
        />
        <textarea 
          placeholder="description" 
          rows={3}
          className="block py-2 px-3 mb-4  w-full   text-black"
          onChange={(e) => setDescription(e.target.value)}
          value={description}
          >
          </textarea>
        <button
        className="bg-white hover:bg-gray-300 text-gray-800 font-semibold py-2 px-4 border border-gray-400 rounded shadow"
        >
          {params.id ? 'Update Task' : 'Create Task'}
        </button>
        </form>
        {
          params.id && (
            <button
              className="bg-red-500 hover:bg-red-400 text-white font-bold py-2 rounded mt-5 px-4"
              onClick={async() => {
                try{
                   const res = await deleteTask(params.id)
                  navigate('/')
                }
                catch(err){
                  console.log(err)
                }
              }}
            >
              Detelete
            </button>
          )
        }
      </div>
    </div>
  )
}

export default TaskForm