"use client"
import { useState } from "react";
import Image from "next/image";
import { TypewriterEffectSmooth } from "@/components/ui/typewriter-effect";
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label";
import { Button } from "@/components/ui/button";
import { WavyBackground } from "@/components/ui/wavy-background";



export default function Home() {
  const [file, setFile] = useState<File>();
  const [loader, setLoader] = useState(true);

const handleFileChange =(event: any)=>{
  setFile(event.target.files?.[0]);
  console.log(event.target.files[0]);

};

const handleSubmit = async (e: React.FormEvent<HTMLFormElement>)=>{
  e.preventDefault();
  if(!file) return;

  try {
    const data = new FormData();
    data.set("file", file);

    const res = await fetch("http://127.0.0.1:8000/api/bill-convertor",{
      method: "POST",
      body: data
    })
    const blob = await res.blob();
    const url = window.URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'bill.xlsx';
    link.click();
    if(!res.ok) throw new Error('something went wrong');
  } catch (e:any){
    console.error(e);
  }

}  


  const words = [
    {
      text: "Add"
    },
    {
      text: "Bills"
    },
    {
      text: "PDF"
    },
    {
      text: "To"
    },
    {
      text: "Get"
    },
    {
      text: "Excel"
    },
    {
      text: "Report"
    },
]
  return (
    <div className="flex flex-col items-center justify-center mt-4 h-[40rem] ">
      <TypewriterEffectSmooth words={words}  />
      <form onSubmit={handleSubmit} className="grid w-full max-w-sm items-center gap-1.5 mt-2 ">
      <Label htmlFor="excel-file">Add your file below</Label>
      <div className="flex w-full max-w-sm items-center gap-1.5 space-x-2">
      
      <Input name="pdf-file" type="file" onChange={handleFileChange}/>
      <Button type="submit" >Submit</Button>

      </div>
    </form>
    </div>
  );
}
