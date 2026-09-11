"use client";

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
import { TextField } from "@/components/ui/text-field";
import { PasswordField } from "@/components/ui/password-field";
import { Button } from "@/components/ui/button";

type LoginFormValues = {
  email: string;
  password: string;
};

export default function LoginForm() {
  const form = useForm<LoginFormValues>({
    defaultValues: { email: "", password: "" },
  });

  function onSubmit(values: LoginFormValues) {
    // اینجا درخواست ورود به سرور بزنید. فعلاً فقط در console چاپ می‌کنیم.
    console.log("login submit:", values);
  }

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="max-w-md mx-auto w-full space-y-6 p-6">
        <FormField
          control={form.control}
          name="email"
          render={({ field }) => (
            <FormItem>
              <FormLabel>ایمیل</FormLabel>
              <FormControl>
                <TextField
                  type="email"
                  placeholder="you@example.com"
                  required
                  value={field.value}
                  onValueChange={field.onChange}
                />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />

        <FormField
          control={form.control}
          name="password"
          render={({ field }) => (
            <FormItem>
              <FormLabel>رمز عبور</FormLabel>
              <FormControl>
                <PasswordField
                  value={field.value}
                  onValueChange={field.onChange}
                  revealToggle
                  // نوار قدرت/قوانین پیش‌فرض را خاموش می‌کنیم برای فرم ورود ساده
                  strength={false}
                  requirements={false}
                />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />

        <div>
          <Button type="submit" fullWidth>
            ورود
          </Button>
        </div>
      </form>
    </Form>
  );
}
