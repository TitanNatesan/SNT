import React, { useState, useEffect, useMemo } from 'react';
import { MantineReactTable, useMantineReactTable } from 'mantine-react-table';
import axios from 'axios';

const DisplayDataFromAPI = () => {
  const [dataFromApi, setDataFromApi] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/getDR/');
        setDataFromApi(response.data);
      } catch (error) {
        console.error('Error fetching data from API:', error.response.data);
        setError('Failed to fetch data from API');
      }
    };

    fetchData();
  }, []);

  const columns = useMemo(
    () => [
      {
        accessorKey: 'product',
        header: 'Product',
      },
      {
        accessorKey: 'number',
        header: 'Number',
      },
      {
        accessorKey: 'quantity',
        header: 'Quantity',
      },
      {
        accessorKey: 'nos',
        header: 'NOS',
      },
      {
        accessorKey: 'consignee_name',
        header: 'Consignee Name',
      },
      {
        accessorKey: 'consignee_code',
        header: 'Consignee Code',
      },
      {
        accessorKey: 'demand_code',
        header: 'Demand Code',
      },
      {
        accessorKey: 'allocation_number',
        header: 'Allocation Number',
      },
      {
        accessorKey: 'accounts_unit',
        header: 'Accounts Unit',
      },
      {
        accessorKey: 'date',
        header: 'Date',
      },
    ],
    []
  );

  const table = useMantineReactTable({
    columns,
    data: dataFromApi,
  });

  return (
    <div className='h-screen'>
      {error && <div>Error: {error}</div>}
      <MantineReactTable table={table} />
    </div>
  );
};

export default DisplayDataFromAPI;
