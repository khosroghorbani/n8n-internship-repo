import React from "react";
import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter } from "@/components/ui/card";
import { TextField } from "@/components/ui/text-field";
import { PasswordField } from "@/components/ui/password-field";
import { Button } from "@/components/ui/button";
import { Alert, AlertTitle, AlertDescription } from "@/components/ui/alert";
import { Link } from "@/components/ui/link";

export default function LoginForm(): JSX.Element {
  const [email, setEmail] = React.useState("");
  const [password, setPassword] = React.useState("");
  const [loading, setLoading] = React.useState(false);
  const [error, setError] = React.useState<string | null>(null);
  const [success, setSuccess] = React.useState<string | null>(null);

  const validate = () => {
    if (!email || !email.includes("@")) {
      setError("آدرس ایمیل معتبر نیست.");
      return false;
    }
    if (!password || password.length < 6) {
      setError("رمز عبور باید حداقل ۶ نویسه باشد.");
      return false;
    }
    return true;
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setSuccess(null);

    if (!validate()) return;

    try {
      setLoading(true);
      // شبیه‌سازی درخواستِ سرور
      await new Promise((res) => setTimeout(res, 800));

      // مثال سادهٔ پاسخ: اگر ایمیل demo@example.com و رمز demo باشد موفق است
      if (email === "demo@example.com" && password === "demo") {
        setSuccess("ورود موفقیت‌آمیز بود.");
      } else {
        setError("ایمیل یا رمز عبور اشتباه است.");
      }
    } catch (err) {
      setError("خطا در برقراری ارتباط. مجدداً تلاش کنید.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="w-full max-w-md mx-auto">
      <Card>
        <CardHeader>
          <CardTitle>ورود به حساب</CardTitle>
          <CardDescription>لطفاً ایمیل و رمز عبور خود را وارد کنید.</CardDescription>
        </CardHeader>

        <CardContent>
          {error && (
            <div className="mb-4">
              <Alert variant="default" color="destructive" dismissible onOpenChange={() => setError(null)}>
                <AlertTitle>خطا</AlertTitle>
                <AlertDescription>{error}</AlertDescription>
              </Alert>
            </div>
          )}

          {success && (
            <div className="mb-4">
              <Alert variant="default" color="success" dismissible onOpenChange={() => setSuccess(null)}>
                <AlertTitle>موفق</AlertTitle>
                <AlertDescription>{success}</AlertDescription>
              </Alert>
            </div>
          )}

          <form onSubmit={handleSubmit} className="flex flex-col gap-4">
            <TextField
              label="ایمیل"
              type="email"
              placeholder="you@example.com"
              value={email}
              onValueChange={(v) => setEmail(String(v))}
              required
            />

            <PasswordField
              label="رمز عبور"
              placeholder="رمز عبور خود را وارد کنید"
              value={password}
              onValueChange={(v) => setPassword(String(v))}
              revealToggle
              required
            />

            <div className="flex items-center justify-between">
              <div />
              <Link href="#" size="sm" underline="hover">
                فراموشی رمز؟
              </Link>
            </div>

            <CardFooter className="pt-2">
              <Button type="submit" fullWidth loading={loading}>
                ورود
              </Button>
            </CardFooter>
          </form>
        </CardContent>
      </Card>
    </div>
  );
}
