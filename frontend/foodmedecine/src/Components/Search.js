import React from 'react'
import TextField from '@mui/material/TextField';
import Stack from '@mui/material/Stack';
import Autocomplete from '@mui/material/Autocomplete';





export const Search = ({name,options}) => {

  
  return (
    <div>
     <Stack spacing={2} sx={{ width: 300 }}>
      <Autocomplete
        id="free-solo-demo"
        freeSolo
        options={options.map((option) => option.title)}
        renderInput={(params) => <TextField {...params} label={name} margin="normal" 
        style={{backgroundColor:"white", borderRadius:"60px"}}
        />}
   
        

      />
      
    </Stack>
    </div>
  )
}
