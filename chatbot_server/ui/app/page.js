"use client";
export default function Home() {
  async function SendPrompt() {
    let message = document.getElementById("message").value;
    let res = await fetch("http://localhost:5000/process-text", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        message,
      }),
    });

    res = await res.json();
    console.log(res);

    let response = JSON.stringify(res.data);
    document.getElementById("response").value = response;
    // console.log(message);
  }

  return (
    <main
      style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        height: "95vh",
      }}
    >
      <div>
        INPUT:
        <input id="message" type="text" />
        <button onClick={SendPrompt}>Send</button>
        <br />
        <br />
        <textarea id="response" cols={50} rows={10} />
      </div>
    </main>
  );
}
