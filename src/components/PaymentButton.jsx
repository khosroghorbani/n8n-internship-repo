import React, { useState } from "react";
import { Button } from "registry/dig/components/ui/button";

export default function PaymentButton({ amount, currency = "تومان", onClick }) {
  const [loading, setLoading] = useState(false);

  async function handleClick(e) {
    if (loading) return;
    setLoading(true);
    try {
      // اگر onClick یک promise برمی‌گرداند، صبر می‌کنیم تا کامل شود.
      const result = onClick ? onClick(e) : new Promise((res) => setTimeout(res, 1200));
      if (result && typeof result.then === "function") {
        await result;
      }
    } finally {
      setLoading(false);
    }
  }

  const label = amount != null ? `پرداخت ${amount} ${currency}` : "پرداخت";

  return (
    <Button onClick={handleClick} loading={loading} color="primary">
      {label}
    </Button>
  );
}
