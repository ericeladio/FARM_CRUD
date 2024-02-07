import axios from "axios"
const URL = 'http://localhost:8000/api/tasks/'

export const getAllTasks = () => axios.get(URL)

export const getTask = (id) => axios.get(`${URL}${id}`)

export const createTask = (newTask) => axios.post(`${URL}`, newTask)

export const editTask = (id, task) =>  axios.put(`${URL}${id}`,task)

export const deleteTask = (id) => axios.delete(`${URL}${id}`)



 
    
