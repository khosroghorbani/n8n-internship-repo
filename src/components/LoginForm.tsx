import React from "react";
import { useForm } from "react-hook-form";
import {
  Form,
  FormField,
  FormItem,
  FormLabel,
  FormControl,
  FormMessage,
} from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import { PasswordField } from "@/components/ui/password-field";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
  CardFooter,
} from "@/components/ui/card";

type LoginFormValues = {
  email: string;
  password: string;
};

export default function LoginForm() {
  const form = useForm<LoginFormValues>({
    defaultValues: {
      email: "",
      password: "",
    },
    mode: "onTouched",
  });

  const onSubmit = async (values: LoginFormValues) => {
    // جای مناسب برای فراخوانی API ورود. اینجا فقط به عنوان نمونه لاگ می‌رویم.
    console.log("login submit", values);
    // شبیه‌سازی تاخیر
    await new Promise((r) => setTimeout(r, 600));
  };

  return (
    <Form {...form}>
      <form
        onSubmit={form.handleSubmit(onSubmit)}
        className="max-w-sm w-full mx-auto"
        noValidate
      >
        <Card>
          <CardHeader>
            <CardTitle>ورود به حساب</CardTitle>
            <CardDescription>با ایمیل و رمز عبور خود وارد شوید.</CardDescription>
          </CardHeader>

          <CardContent>
            <div className="grid gap-4">
              <FormField
                name="email"
                control={form.control}
                rules={{
                  required: "ایمیل لازم است",
                  pattern: {
                    value: /\S+@\S+\.\S+/,
                    message: "ایمیل معتبر نیست",
                  },
                }}
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>ایمیل</FormLabel>
                    <FormControl>
                      <Input
                        placeholder="you@example.com"
                        type="email"
                        {...field}
                      />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />

              <FormField
                name="password"
                control={form.control}
                rules={{
                  required: "رمز عبور لازم است",
                  minLength: { value: 8, message: "حداقل ۸ کاراکتر لازم است" },
                }}
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>رمز عبور</FormLabel>
                    <FormControl>
                      <PasswordField
                        // PasswordField از onValueChange استفاده می‌کند
                        value={field.value}
                        onValueChange={field.onChange}
                        placeholder="رمز عبور"
                        revealToggle
                      />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />
            </div>
          </CardContent>

          <CardFooter>
            <Button
              type="submit"
              fullWidth
              loading={form.formState.isSubmitting}
            >
              ورود
            </Button>
          </CardFooter>
        </Card>
      </form>
    </Form>
  );
}
