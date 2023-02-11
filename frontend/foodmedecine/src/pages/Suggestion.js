import { Grid } from '@mui/material'
import React from 'react'
import Cards from '../Components/Cards'

export const Suggestion = () => {
  return (
    <div >
       <Grid container spacing={2}>
        <Grid item xs={12} sm={6} md={4}>
            <Cards />
        </Grid>

        <Grid item xs={12} sm={6} md={4}>
            <Cards />
            </Grid>

        <Grid item xs={12} sm={6} md={4}>
            <Cards />
            </Grid>

            <Grid item xs={12} sm={6} md={4}>
            <Cards />
            </Grid>
        </Grid>
        

    </div>
  )
}
