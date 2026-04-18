import React, { useEffect, useState } from 'react';

const Users = () => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setUsers(results);
        console.log('Users API endpoint:', endpoint);
        console.log('Fetched users:', results);
        setLoading(false);
      })
      .catch(err => {
        console.error('Error fetching users:', err);
        setLoading(false);
      });
  }, [endpoint]);

  if (loading) return <div className="text-center my-4"><div className="spinner-border" role="status"><span className="visually-hidden">Loading users...</span></div></div>;

  return (
    <div className="card mb-4">
      <div className="card-header bg-secondary text-white">
        <h2 className="h4 mb-0">Users</h2>
      </div>
      <div className="card-body">
        <div className="table-responsive">
          <table className="table table-striped table-bordered align-middle">
            <thead className="table-light">
              <tr>
                <th scope="col">#</th>
                <th scope="col">Username</th>
              </tr>
            </thead>
            <tbody>
              {users.map((user, idx) => (
                <tr key={user.id || idx}>
                  <td>{idx + 1}</td>
                  <td>{user.username || user.name || JSON.stringify(user)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default Users;
