import sqlite3 from 'sqlite3';
import {fileURLToPath} from 'url';
import path from 'path';
import express from 'express';
import cors from 'cors';

const __fileName=fileURLToPath(import.meta.url)
const __dirName=path.dirname(__fileName)

const dbPath=path.resolve(__dirName,"user_database.db")
const db=new sqlite3.Database(dbPath,sqlite3.OPEN_READWRITE,(err)=>{
    if(err){
        console.error(err.message)
    }else{
        console.log("Connected to SQL Database")
    }
})

const app=express()
app.use(cors)
app.use(express.json)
app.use(express.urlencoded({extended:true}))

app.get('/users', (req, res)=>{
    db.all(`SELECT * FROM Users`,[],(err,rows)=>{
        if (err){
            console.error(err.message)
            res.status(500).send("Error retrieving users from database")
        }else{
            res.status(200).jason(rows)
        }
    })
})

app.post("/addUser",(req, res)=>{
    const{username, email}=req.body
    db.run(`INSERT INTO Users (username, email) VALUES(?,?)`,[username, email],function(err){
        if (err){
            console.error(err.message)
            res.status(500).send("Error adding user to databaser")
        }else{
            console.log(`A new user has been added with ID: ${this.lastID}`)
            res.status(200).send("User added succesfully")
        }
})
})

const PORT=3000
app.listen(PORT,()=>{
    console.log(`Server is runnnung on port ${PORT}`)
})