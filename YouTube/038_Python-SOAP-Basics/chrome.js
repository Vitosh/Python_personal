function soapCalc(op, a, b) {
  const xml = `<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
               xmlns:xsd="http://www.w3.org/2001/XMLSchema"
               xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <${op} xmlns="http://tempuri.org/">
      <intA>${a}</intA>
      <intB>${b}</intB>
    </${op}>
  </soap:Body>
</soap:Envelope>`;

  return fetch("/calculator.asmx", {
    method: "POST",
    headers: {
      "Content-Type": "text/xml; charset=utf-8",
      "SOAPAction": `http://tempuri.org/${op}`
    },
    body: xml
  })
  .then(r => r.text())
  .then(str => {
    const doc = new DOMParser().parseFromString(str, "text/xml");
    const resultTag = `${op}Result`;
    const result = doc.getElementsByTagName(resultTag)[0]?.textContent;
    console.log(`${op}(${a}, ${b}) → ${result}`);
    return Number(result);
  });
}

const soapAdd      = (a,b) => soapCalc("Add", a, b);
const soapSubtract = (a,b) => soapCalc("Subtract", a, b);
const soapMultiply = (a,b) => soapCalc("Multiply", a, b);
const soapDivide   = (a,b) => soapCalc("Divide", a, b);

soapMultiply(6, 7) //42
